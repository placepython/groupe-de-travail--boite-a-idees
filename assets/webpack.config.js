const path = require('path');
const { merge } = require('webpack-merge');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = ({ mode }) => {
    return merge({
        mode: `${mode}`,
        entry: {
            main: path.resolve(__dirname, 'src/index')
        },
        output: {
            path: path.resolve(__dirname, './dist'),
            filename: '[name].[contenthash].bundle.js',
            publicPath: '/static/',
            clean: true
        },
        module: {
            rules: [
                {
                    test: /\.js$/i,
                    use: 'babel-loader'
                },
                {
                    test: /\.ts$/i,
                    use: 'ts-loader'
                },
                {
                    test: /\.(scss|css)$/i,
                    use: [
                        MiniCssExtractPlugin.loader,
                        "css-loader",
                        "postcss-loader",
                        {
                            loader: 'sass-loader',
                            options: {
                               sourceMap: true,
                            }
                        }
                    ]
                },
                {
                    test: /\.(png|svg|jpg|jpeg|gif)$/i,
                    type: 'asset/resource',
                    generator: {
                        filename: 'images/[name].[hash][ext][query]'
                    }
                },
                {
                    test: /\.(woff|woff2|eot|ttf|otf)$/i,
                    type: 'asset/resource',
                    generator: {
                        filename: 'fonts/[name].[hash][ext][query]'
                    }
                }
            ]
        },
        plugins: [
            new MiniCssExtractPlugin({
                filename: "css/[name].[contenthash].css",
                chunkFilename: "[id].css"
            }),
            new BundleTracker({
                filename: 'webpack-stats.json', 
                relativePath: true
            })
        ]
    }, require(`./build-utils/webpack/${mode}`));
};